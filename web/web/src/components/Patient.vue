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
        <a href="#" class="btn btn-primary">Edit</a>
        <a href="#" class="btn btn-primary">Delete</a>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  data () {
    return {
      patient: {}
    }
  },
  computed: {
    ...mapState([
      'patients'
    ])
  },
  mounted () {
    const patient = this.patients[this.$route.params.id]
    this.patient = patient
    console.log(patient)
  }
}
</script>

<style>
  a.btn{
    margin: 0 0.5rem;
  }
</style>
