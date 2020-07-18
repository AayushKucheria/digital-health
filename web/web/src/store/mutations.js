export default {
  SET_PATIENTS (state, patients) {
    state.patients = patients
  },
  SET_PATIENT (state, patient) {
    state.patient = patient
  },
  ADD_PATIENT: (state, patient) => {
    state.patients.unshift(patient)
  }
}
