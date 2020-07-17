import axios from 'axios'

export default axios.create({
  baseURL: 'http://127.0.0.1:8000/patients',
  headers: {
    'Access-Control-Allow-Origin': '*',
    Accept: '*/*',
    'Content-type': 'application/json'
  }
})
