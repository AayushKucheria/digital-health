<template>
  <div class="addPatient">
    <button @click= "togglePatientForm" class = "btn btn-primary">Add New Patient</button>

        <b-form @submit.prevent="handleSubmit" v-if="showPatientForm">
          <b-form-group id="input-group-2" label="Patient's Name:" label-for="input-2">
            <b-form-input
              id="input-2"
              type="text"
              v-model="formData.name"
              required
              placeholder="Enter patient name"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Patient's Age:" label-for="input-3">
            <b-form-input
              id="input-3"
              type="number"
              v-model="formData.age"
              required
              placeholder="Enter patient age"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-4" label="Gender:" label-for="input-4">
            <b-form-select
              id="input-4"
              v-model="formData.gender"
              :options="['male', 'female']"
              required
            ></b-form-select>
          </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'addPatient',
  data () {
    return {
      showPatientForm: false,
      formData: {
        name: '',
        age: 0,
        gender: null
      }
    }
  },
  methods: {
    ...mapActions([
      'addPatient'
    ]),
    togglePatientForm () {
      this.showPatientForm = !this.showPatientForm
    },
    handleSubmit () {
      const { name, age, gender } = this.formData
      const payload = {
        name,
        age,
        gender
      }
      this.addPatient(payload)

      this.formData = {
        name: '',
        age: 0,
        gender: null
      }
    }
  }
}
</script>
