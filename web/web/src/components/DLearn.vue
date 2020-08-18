<template>
  <div class="result">
    <div class="card">
      <div class="card-header">
        <h2>Deep Learning Result</h2>
      </div>
      <div class="card-body">
        <div v-if="results">
          <h5>Patient ID: {{ results.patient_id }} </h5>
          <h5>Session ID: {{ results.session_id }} </h5>
          <h5>Result: {{ results.result }} </h5>
        </div>
        <div v-else>Error loading result.</div>
      </div>
    </div>
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
      'loadDLResult'
    ])
  },
  computed: {
    ...mapState([
      'results'
    ])
  },
  created () {
    this.loadDLResult(this.$route.params.id)
  }
}
</script>
