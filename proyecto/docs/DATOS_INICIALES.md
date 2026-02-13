# Datos iniciales

La aplicación usa una DB en memoria (`infrastructure/db.py`) que se inicializa como Singleton.

## Usuario por defecto
- `id`: 6d976e5f-85ab-4bce-8c0f-aa9270eaa308
- `username`: `admin`
- `password`: `1234`
- `rol`: `ADMIN` (valor numérico `1`)

## Estructuras iniciales
- `users` contiene al usuario `admin`.
- `clocks` contiene la clave del `admin` con lista vacía: `{ '<admin-id>': [] }`.

> Nota: Los datos están en memoria y **no** se persisten entre ejecuciones.
