export default {
  addPatient: ({ commit }, payload) => {
    commit('appendPatient', payload)
  }
}
