from pathlib import Path
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
import matplotlib.pyplot as plt

# -----------------------------
# Configuración general
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "data" / "dataset_cacao"
MODEL_DIR = BASE_DIR / "ml" / "model"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS_INICIALES = 10
EPOCHS_FINE_TUNING = 5
CLASES = ["Bueno", "Regular", "Malo"]

# -----------------------------
# Carga de datos
# -----------------------------
train_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR / "train",
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="categorical",
    shuffle=True,
)

val_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR / "val",
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="categorical",
    shuffle=False,
)

test_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_DIR / "test",
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="categorical",
    shuffle=False,
)

class_names = train_ds.class_names
print("Clases detectadas:", class_names)

AUTOTUNE = tf.data.AUTOTUNE
train_ds = train_ds.prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.prefetch(buffer_size=AUTOTUNE)
test_ds = test_ds.prefetch(buffer_size=AUTOTUNE)

# -----------------------------
# Aumento de datos
# -----------------------------
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal"),
    layers.RandomRotation(0.08),
    layers.RandomZoom(0.10),
    layers.RandomContrast(0.10),
])

# -----------------------------
# Modelo base preentrenado
# -----------------------------
base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)
base_model.trainable = False

inputs = layers.Input(shape=(224, 224, 3))
x = data_augmentation(inputs)
x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
x = base_model(x, training=False)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.3)(x)
outputs = layers.Dense(len(CLASES), activation="softmax")(x)

model = models.Model(inputs, outputs)

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# -----------------------------
# Entrenamiento inicial
# -----------------------------
callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=3,
        restore_best_weights=True
    ),
    tf.keras.callbacks.ModelCheckpoint(
        filepath=str(MODEL_DIR / "mejor_modelo.keras"),
        monitor="val_accuracy",
        save_best_only=True
    )
]

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS_INICIALES,
    callbacks=callbacks
)

# -----------------------------
# Fine-tuning
# -----------------------------
base_model.trainable = True

for layer in base_model.layers[:-35]:
    layer.trainable = False

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

history_ft = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS_FINE_TUNING,
    callbacks=callbacks
)

# -----------------------------
# Evaluación final
# -----------------------------
test_loss, test_acc = model.evaluate(test_ds)
print(f"Precisión en test: {test_acc:.4f}")
print(f"Pérdida en test: {test_loss:.4f}")

# Guardar modelo final
model.save(MODEL_DIR / "cacao_classifier.keras")

# Guardar etiquetas
with open(MODEL_DIR / "labels.txt", "w", encoding="utf-8") as f:
    for clase in class_names:
        f.write(clase + "\n")

# -----------------------------
# Gráficas
# -----------------------------
acc = history.history["accuracy"] + history_ft.history["accuracy"]
val_acc = history.history["val_accuracy"] + history_ft.history["val_accuracy"]
loss = history.history["loss"] + history_ft.history["loss"]
val_loss = history.history["val_loss"] + history_ft.history["val_loss"]

plt.figure(figsize=(10, 4))
plt.plot(acc, label="Entrenamiento")
plt.plot(val_acc, label="Validación")
plt.title("Precisión del modelo")
plt.xlabel("Época")
plt.ylabel("Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig(MODEL_DIR / "grafica_accuracy.png")
plt.close()

plt.figure(figsize=(10, 4))
plt.plot(loss, label="Entrenamiento")
plt.plot(val_loss, label="Validación")
plt.title("Pérdida del modelo")
plt.xlabel("Época")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig(MODEL_DIR / "grafica_loss.png")
plt.close()

print("Entrenamiento terminado.")