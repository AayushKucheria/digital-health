export default {
  SET_PATIENTS (state, patients) {
    state.patients = patients
  },
  appendPatient: (state, patient) => {
    state.patients.push(patient)
  }
}
