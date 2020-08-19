<template>
  <div class="patient">

    <div class="card">
      <div class="card-header">
        <h2>Patient Information</h2>
      </div>
      <div class="card-body">
        <h5>Patient ID: {{ patient.id }} </h5>
        <h5>Name: {{ patient.name }} </h5>
        <h5>Age: {{ patient.age }} </h5>
        <h5>Gender: {{ patient.sex }} </h5>
        <br>
        <div class="btns">
          <b-button variant="success" class="btns" @click="$router.push(`${patient.id}/dlearn`)">Result Deep Learn</b-button>
          <b-button variant="success" class="btns" @click="$router.push(`${patient.id}/kmean`)">Result K-Mean</b-button>
          <b-button variant="danger" class="btns" @click.prevent="deletepatient">Delete</b-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
export default {
  data () {
    return {
      patient: {}
    }
  },
  computed: {
    ...mapState([
      'patients'
    ]),
    ...mapGetters([
      'patientsList',
      'getPatientById'
    ])
  },
  methods: {
    ...mapActions([
      'loadPatient',
      'loadPatients',
      'deletePatient',
      'deletePatient'
    ]),
    deletepatient () {
      this.deletePatient(this.patient.id)
    }
  },
  created () {
    const patient = this.patients[this.$route.params.id]
    this.patient = patient
    console.log(this.patient.id)
  }
}
</script>

<style>
  a.btn{
    margin: 0 0.5rem;
    padding: 0 0.5rem;
  }
  .btns{
    margin: 0 0.5rem;
    padding: 0.5 1rem;
  }
  .card{
    margin-top: 2rem;
  }
  .card-header{
    background-color: rgb(231, 243, 245);
  }
</style>
