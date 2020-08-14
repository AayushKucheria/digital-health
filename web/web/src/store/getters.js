
export default {
  patientsList: state => state.patients,
  getPatientById: (state) => (id) => {
    return state.patients.find(patient => patient.id === id)
  }
}
