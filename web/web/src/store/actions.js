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
  async addPatient ({ commit }, payload) {
    await PatientDataService.create(payload)
      .then(res => {
        console.log(res)
        console.log(res.data)
        commit('appendPatient', res.data)
      })
      .catch(err => {
        console.log('Network error')
        console.log(err)
      })
  }
}
