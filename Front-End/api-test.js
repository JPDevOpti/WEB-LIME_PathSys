// Test API call
import axios from 'axios'

const API_URL = 'http://localhost:8000/api/v1'

console.log('Testing API connection...')
console.log('API_URL:', API_URL)

// Test pacientes endpoint directly
axios.get(`${API_URL}/pacientes/cedula/12345678`)
  .then(response => {
    console.log('✅ Pacientes endpoint success:', response.data)
  })
  .catch(error => {
    console.error('❌ API Error:', error.message)
    console.error('Error details:', error.response?.data || error)
    
    if (error.code === 'NETWORK_ERROR' || error.message.includes('Network Error')) {
      console.log('🔍 This is a network error. Possible causes:')
      console.log('  1. Backend not running')
      console.log('  2. CORS issues')
      console.log('  3. Firewall blocking connection')
      console.log('  4. Incorrect API URL')
    }
  })
