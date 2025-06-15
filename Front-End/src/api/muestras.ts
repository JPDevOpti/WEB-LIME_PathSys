// src/api/muestras.ts
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

export interface MuestraFormData {
  numeroMuestras: string
  muestras: {
    numero: number
    regionCuerpo: string
    cups: { code: string, cantidad: number }[]
  }[]
  medicoSolicitante: string
  fechaIngreso: string
  pacienteId: string
  // Agregar nuevos campos
  nombrePaciente: string
  entidad: string
  observaciones?: string
}

// Función auxiliar para convertir fecha del formato DD/MM/YYYY HH:MM a ISO
const parseSpanishDateToISO = (fechaEspanol: string): string => {
  try {
    // Formato esperado: DD/MM/YYYY HH:MM
    const [datePart, timePart] = fechaEspanol.split(' ')
    const [day, month, year] = datePart.split('/').map(Number)
    const [hours, minutes] = timePart.split(':').map(Number)
    
    // Crear fecha en formato ISO
    const fecha = new Date(year, month - 1, day, hours, minutes)
    
    if (isNaN(fecha.getTime())) {
      throw new Error('Fecha inválida')
    }
    
    return fecha.toISOString()
  } catch (error) {
    console.error('Error parsing date:', fechaEspanol, error)
    throw new Error(`Formato de fecha inválido: ${fechaEspanol}. Use DD/MM/YYYY HH:MM`)
  }
}

export const crearSolicitudMuestras = async (data: MuestraFormData) => {
  // Transformar los datos del frontend al formato del backend
  const backendData = {
    medico_solicitante: data.medicoSolicitante || null,
    fecha_ingreso: parseSpanishDateToISO(data.fechaIngreso),
    observaciones: data.observaciones || null,
    // Agregar nombre del paciente y entidad
    nombre_paciente: data.nombrePaciente,
    entidad: data.entidad,
    muestras: data.muestras.map(muestra => ({
      numero: muestra.numero,
      region_cuerpo: muestra.regionCuerpo,
      cups: muestra.cups
    })),
    usuario_id: "temp_user_id", // TODO: Obtener del contexto de usuario
    paciente_id: data.pacienteId
  }
  
  const response = await axios.post(`${API_URL}/muestras/`, backendData)
  return response.data
}

export const listarMuestras = async () => {
  const response = await axios.get(`${API_URL}/muestras/`)
  return response.data
}
