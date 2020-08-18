<template>
  <div>
    <h1> K-Mean Result</h1>
      <div v-if="results">
        <h5>Patient ID: {{ results.patient_id }} </h5>
        <h5>Session ID: {{ results.session_id }} </h5>
        <h5>Result: {{ results.result }} </h5>
      </div>
      <div v-else>Error loading result.</div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'results',
  data () {
    return {
      result: {
        patient_id: 0,
        model_id: 0,
        result: 0,
        session_id: 0
      }
    }
  },
  methods: {
    ...mapActions([
      'loadKMResult'
    ])
  },
  computed: {
    ...mapState([
      'results'
    ])
  },
  created () {
    this.loadKMResult(this.$route.params.id)
    // this.results = results
    console.log(this.results)
  }
}
</script>
