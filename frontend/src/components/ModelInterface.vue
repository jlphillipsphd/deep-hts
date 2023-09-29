<template>
  <div class="model-interface">
    <h2>Model Interface</h2>
    <p>Upload your DNA sequencing data to get predictions from our model:</p>
    <input type="file" @change="handleFileUpload">
    <button @click="submitData" hx-post="/get_prediction" hx-target="#results">Get Prediction</button>
    <div id="results">
      <!-- Model results will be displayed here -->
    </div>
  </div>
</template>

<script>
export default {
  name: 'ModelInterface',
  data() {
    return {
      file: null
    }
  },
  methods: {
    handleFileUpload(event) {
      this.file = event.target.files[0];
    },
    submitData() {
      // Here you can handle the file data, for instance, 
      // send it to the Flask backend via an AJAX call.
      // Note: The AJAX functionality would be outside of HTMX, so you'd use something like axios.
      if (this.file) {
        let formData = new FormData();
        formData.append('file', this.file);
        
        // Use axios or another AJAX library to send the file to the server.
        // The actual AJAX call implementation is not shown here for brevity.
      }
    }
  }
}
</script>

<style scoped>
/* Scoped CSS styles specific to this component */
.model-interface {
  padding: 20px;
  border: 1px solid #ddd;
  margin-top: 20px;
}
</style>
