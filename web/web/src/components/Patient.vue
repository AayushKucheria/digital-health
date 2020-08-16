<template>
  <div class="patient">

    <div class="card">
      <div class="card-header">
        <h2>Patient Information</h2>
      </div>
      <div class="card-body">
        <h5>
          <div class="infoText" v-for="(name, value) in patient" :key="name.id">
            {{value}}: {{name}}
          </div>
        </h5>
        <div class="btns">
          <b-button variant="success" class="btns" @click="$router.push(`${patient.id}/dlearn`)">Run Deep Learn</b-button>
          <b-button variant="success" class="btns" @click="$router.push(`${patient.id}/kmean`)">Run K-Mean</b-button>
          <b-button variant="success" class="btns" @click="$router.push('upload')">Upload session</b-button>
          <b-button variant="info" class="btns" @click.prevent="getEdit">Edit</b-button>
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
      this.loadPatient(this.$route.params.id)
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
