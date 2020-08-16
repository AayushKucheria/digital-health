export default {
  GET_PATIENTS: (state, patients) => {
    state.patients = patients
  },
  GET_PATIENT: (state, patient) => {
    state.patient = patient
  },
  ADD_PATIENT: (state, patient) => {
    state.patients.unshift(patient)
  },
  GET_RESULT: (state, result) => {
    state.results.unshift(result)
  },
  REMOVE_PATIENT: (state, id) => {
    state.patients.filter(patient => patient.id !== id)
    state.patients.splice(patient => patient.id, 1) // remove the patient with found ID
  }
}
