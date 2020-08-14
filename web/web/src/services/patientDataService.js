import axios from 'axios'

var instance = axios.create({
  baseURL: 'http://127.0.0.1:8000/patients',
  headers: {
    // 'Access-Control-Allow-Origin': '*',
    // Accept: '*/*',
    // 'Content-type': 'application/json, application/x-www-form-urlencoded'
  }
})

class PatientDataService {
  getAll () {
    instance.defaults.timeout = 2500
    return instance.get('/')
  }

  get (id) {
    return instance.get(`/${id}`) // Alright... I've been trying to get the real ID from a specific patient when clicked... Just get it now.  Now I can get access to patient with ID. There is logic for delete also. So I'll need to work on make that happens and then find a way to run model from front end
  }

  create (data) {
    return instance.post('/', data)
  }

  update (id, data) {
    return instance.put(`/${id}`, data)
  }

  delete (id) {
    return instance.delete(`/${id}`)
  }
}

export default new PatientDataService()
