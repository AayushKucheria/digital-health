export default {
  SET_PATIENTS (state, patients) {
    state.patients = patients
  },
  ADD_PATIENT: (state, patient) => {
    state.patients.unshift(patient)
  }
}
