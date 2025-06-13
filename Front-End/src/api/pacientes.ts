// src/api/pacientes.ts
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

export const crearPaciente = async (paciente: any) => {
  const response = await axios.post(`${API_URL}/pacientes/`, paciente)
  return response.data
}

export const buscarPacientePorCedula = async (numeroCedula: string) => {
  try {
    const response = await axios.get(`${API_URL}/pacientes/cedula/${numeroCedula}`)
    return response.data
  } catch (error) {
    if (error.response?.status === 404) {
      return null // Paciente no encontrado
    }
    throw error
  }
}
