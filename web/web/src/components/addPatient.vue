<template>
  <div class="addPatient">
    <button @click= "togglePatientForm" class = "btn btn-primary">Add New Patient</button>

        <b-form @submit.prevent="handleSubmit" v-if="showPatientForm">
          <b-form-group id="input-group-1" label="Patient's Name:" label-for="input-1">
            <b-form-input
              id="input-1"
              type="text"
              v-model="formData.name"
              required
              placeholder="Enter patient name"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Patient's Age:" label-for="input-2">
            <b-form-input
              id="input-2"
              type="number"
              step="1"
              v-model.number="formData.age"
              required
              placeholder="Enter patient age"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Gender:" label-for="input-3">
            <b-form-select
              id="input-3"
              v-model="formData.sex"
              :options="['Male', 'Female']"
              required
            ></b-form-select>
          </b-form-group>

          <b-form-group id="input-group-4" label="Patient's ID:" label-for="input-4">
            <b-form-input
              id="input-4"
              type="number"
              step="1"
              v-model.number="formData.id"
              required
              placeholder="Enter a unique ID for patient"
            ></b-form-input>
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
        sex: '',
        age: 0,
        name: '',
        id: 0
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
      const { sex, age, name, id } = this.formData
      const payload = {
        sex,
        age,
        name,
        id
      }
      this.addPatient(payload)
      this.formData = {
        sex: '',
        age: 0,
        name: '',
        id: 0
      }
    }
  }
}
</script>
