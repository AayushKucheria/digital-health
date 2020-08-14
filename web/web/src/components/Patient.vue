<template>
  <div class="patient">

    <div class="card">
      <div class="card-header">
        <h2>Patient Information</h2>
      </div>
      <div class="card-body">
          <h5>ID: {{ patient.id }}</h5>
          <h5>Patient name: {{ patient.name}}</h5>
          <h5>Gender: {{ patient.sex}}</h5>
          <h5>Age: {{ patient.age}}</h5>
          <h5>Record: {{ patient.record}}</h5>
          <br>
        <div class="btns">
          <b-button variant="info" class="btns">Run Model</b-button>
          <b-button
          variant="success"
          class="btns"
          @click="getEdit">Edit</b-button>
          <b-button variant="danger" class="btns">Delete</b-button>
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
      'deletePatient'
    ]),
    getEdit () {
      console.log('edit')
      console.log(this.patient.id)
      this.loadPatient(this.patient.id)
    }
  },
  created () {
    const patient = this.patients[this.$route.params.id]
    this.patient = patient
    // console.log(this.patient.id)
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
