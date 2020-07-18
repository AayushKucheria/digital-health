import PatientDataService from '../services/patientDataService'

export default {
  async loadPatients ({ commit }) {
    await PatientDataService.getAll()
      .then(res => {
        console.log(res)
        console.log(res.data)
        commit('SET_PATIENTS', res.data)
      })
      .catch(err => {
        console.log('Network error')
        console.log(err)
      })
  },
  // TO DO: Load patient by ID
  async loadPatient ({ commit }, id) {
    await PatientDataService.get(id)
      .then(res => {
        console.log(res)
        console.log(res.data)
        commit('SET_PATIENT', res.data)
      })
      .catch(err => {
        console.log('Network error')
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
        console.log('Network error')
        console.log(err)
      })
  }
  //  TO DO: EDIT and DELETE patient by ID
}
