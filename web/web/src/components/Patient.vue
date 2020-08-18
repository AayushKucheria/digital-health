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
          <b-button variant="success" class="btns" @click="$router.push(`${patient.id}/dlearn`)">Run Deep Learn</b-button>
          <b-button variant="success" class="btns" @click="$router.push(`${patient.id}/kmean`)">Run K-Mean</b-button>
          <b-button variant="info" class="btns" @click.prevent="getEdit">Edit</b-button>
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
      'deletePatient',
      'deletePatient'
    ]),
    deletepatient () {
      console.log(this.patient.id)
      this.deletePatient(this.$route.params.id)
    }
  },
  created () {
    const patient = this.patients[this.$route.params.id]
    this.patient = patient
    console.log(this.patient.id)
    // var id = this.getPatientById(this.patient.id)
    // console.log(id)
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
</style>
