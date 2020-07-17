<template>
  <div class="patient">
    <h1> Information about patient </h1>
    <p>{{ patient.id }}
    <br>{{ patient.name }}
    <br>{{ patient.gender }}
    <br>{{ patient.age }}
    <br>{{ patient.record }}
    <br>{{ patient.result }}
    </p>
    <p> This page will be used for edit patient, add record  </p>
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
      'dummyPatients'
    ])
  },
  mounted () {
    const patient = this.dummyPatients[this.$route.params.id]
    this.patient = patient
    console.log(patient)
  }
}
</script>
