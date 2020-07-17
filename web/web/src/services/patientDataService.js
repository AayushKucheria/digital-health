import axios from 'axios'

var instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/patients',
  headers: {
    'Access-Control-Allow-Origin': '*',
    Accept: '*/*',
    'Content-type': 'application/json, application/x-www-form-urlencoded'
  }
})

class PatientDataService {
  getAll () {
    instance.defaults.timeout = 2500
    return instance.get('/')
  }

  get (id) {
    return instance.get('/$id')
  }

  create (data) {
    return instance.post('/', data)
  }

  update (id, data) {
    return instance.put('/$id', data)
  }

  delete (id) {
    return instance.delete('/$id')
  }
}

export default new PatientDataService()
