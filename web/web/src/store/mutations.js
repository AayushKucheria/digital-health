export default {
  SET_PATIENTS: (state, patients) => {
    state.patients = patients
  },
  SET_PATIENT: (state, patient) => {
    state.patient = patient
  },
  ADD_PATIENT: (state, patient) => {
    state.patients.unshift(patient)
  },
  REMOVE_PATIENT: (state, id) => {
    state.patients.filter(patient => patient.id !== id)
    state.patients.splice(patient => patient.id, 1) // remove the patient with found ID
  }
}
