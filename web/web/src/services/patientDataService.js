import axios from '../http-common'

class PatientDataService {
  getAll () {
    return axios.get('/')
  }

  get (id) {
    return axios.get('/$id')
  }

  create (data) {
    return axios.post('/', data)
  }

  update (id, data) {
    return axios.put('/$id', data)
  }

  delete (id) {
    return axios.delete('/$id')
  }
}

export default new PatientDataService()
