<template>
  <div class="result">
    <div class="card">
      <div class="card-header">
        <h2>K-Mean Result</h2>
      </div>
      <div class="card-body">
        <div v-if="results && results.model_id==0">
          <h5>Patient ID: {{ results.patient_id }} </h5>
          <h5>Session ID: {{ results.session_id }} </h5>
          <h5>Result: {{ results.result }} </h5>
          <p v-if="results.result == 0"> 0 means patient is not having epileptic seisure. </p>
          <p v-else> 1 means patient is having epileptic seisure. </p>

        </div>
        <div v-else>No result for K-Mean model found for this patient.</div>
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
    console.log(this.results)
  }
}
</script>

<style>
  .card{
    margin-top: 2rem;
  }
  .card-header{
    background-color: rgb(231, 243, 245);
  }
  p{
    font-style: italic;
  }
</style>
