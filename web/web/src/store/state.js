import PatientDataService from '../services/patientDataService'

export default {
  async retrievePatients () {
    await PatientDataService.getAll()
      .then(res => {
        console.log(res)
        this.patients = JSON.stringify(res.data)
        console.log(res.data)
      })
      .catch(err => {
        console.log('Network error')
        console.log(err)
      })
  }
}
