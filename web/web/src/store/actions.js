import PatientDataService from '../services/patientDataService'

export default {
  async loadPatients ({ commit }) {
    await PatientDataService.getAll()
      .then(res => {
        console.log(res)
        console.log(res.data)
        commit('GET_PATIENTS', res.data)
      })
      .catch(err => {
        console.log('Network error when fetch all patients')
        console.log(err)
      })
  },
  // TODO: Load patient by ID
  async loadPatient ({ commit }, id) {
    await PatientDataService.get(id)
      .then(res => {
        console.log(res)
        console.log(res.data)
        commit('GET_PATIENT', id)
      })
      .catch(err => {
        console.log('Network error when fetch 1 patient')
        console.log(err)
      })
  },
  async addPatient ({ commit }, payload) {
    await PatientDataService.create(payload)
      .then(res => {
        console.log(res)
        commit('ADD_PATIENT', res.data)
      })
      .catch(err => {
        console.log('Network error when adding patient')
        console.log(err)
      })
  },
  // Get KM model result
  async loadKMResult ({ commit }, id) {
    await PatientDataService.getKMResult(id)
      .then(res => {
        console.log(res)
        console.log(res.data)
        commit('GET_RESULT', id)
      })
      .catch(err => {
        console.log('Network error when fetch 1 patient')
        console.log(err)
      })
  },
  // Get DL Model result
  async loadDLResult ({ commit }, id) {
    await PatientDataService.getDLResult(id)
      .then(res => {
        console.log(res)
        console.log(res.data)
        commit('GET_RESULT', id)
      })
      .catch(err => {
        console.log('Network error when fetch 1 patient')
        console.log(err)
      })
  },
  //  TODO: EDIT and DELETE patient by ID
  async deletePatient ({ commit }, id) {
    await PatientDataService.delete(id)
      .then(res => {
        console.log(res)
        console.log(res.data)
        commit('REMOVE_PATIENT', id)
      })
      .catch(err => {
        console.log('Network error when delete 1 patient')
        console.log(err)
      })
  }
}
