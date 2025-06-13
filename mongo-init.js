// Script de inicialización para MongoDB
db = db.getSiblingDB('lime_pathsys');

// Crear usuario para la aplicación
db.createUser({
  user: 'app_user',
  pwd: 'app_password',
  roles: [
    {
      role: 'readWrite',
      db: 'lime_pathsys'
    }
  ]
});

// Crear colecciones con validación
db.createCollection('usuarios', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['nombre', 'email', 'rol', 'password'],
      properties: {
        nombre: {
          bsonType: 'string',
          description: 'Nombre del usuario es requerido'
        },
        email: {
          bsonType: 'string',
          pattern: '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
          description: 'Email válido es requerido'
        },
        rol: {
          bsonType: 'string',
          enum: ['admin', 'patologo', 'tecnico', 'usuario'],
          description: 'Rol debe ser uno de: admin, patologo, tecnico, usuario'
        },
        password: {
          bsonType: 'string',
          description: 'Password es requerido'
        },
        activo: {
          bsonType: 'bool',
          description: 'Estado activo del usuario'
        }
      }
    }
  }
});

db.createCollection('muestras', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['codigo', 'tipo', 'ubicacion', 'fecha_recoleccion', 'usuario_id'],
      properties: {
        codigo: {
          bsonType: 'string',
          description: 'Código de muestra es requerido'
        },
        tipo: {
          bsonType: 'string',
          enum: ['Suelo', 'Agua', 'Aire', 'Tejido', 'Sangre', 'Orina', 'Otros'],
          description: 'Tipo de muestra es requerido'
        },
        ubicacion: {
          bsonType: 'string',
          description: 'Ubicación de recolección es requerida'
        },
        fecha_recoleccion: {
          bsonType: 'date',
          description: 'Fecha de recolección es requerida'
        },
        estado: {
          bsonType: 'string',
          enum: ['pendiente', 'en_proceso', 'procesada', 'completada', 'rechazada'],
          description: 'Estado de la muestra'
        },
        usuario_id: {
          bsonType: 'string',
          description: 'ID del usuario que registró la muestra'
        }
      }
    }
  }
});

// Crear índices
db.usuarios.createIndex({ email: 1 }, { unique: true });
db.usuarios.createIndex({ nombre: 1 });
db.usuarios.createIndex({ rol: 1 });

db.muestras.createIndex({ codigo: 1 }, { unique: true });
db.muestras.createIndex({ tipo: 1 });
db.muestras.createIndex({ estado: 1 });
db.muestras.createIndex({ fecha_recoleccion: 1 });
db.muestras.createIndex({ usuario_id: 1 });

print('Base de datos inicializada correctamente');
