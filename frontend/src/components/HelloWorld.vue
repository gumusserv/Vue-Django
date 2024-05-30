<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  data() {
    return {
      items: []
    }
  },
  methods: {
    fetchItems() {
      axios.get('http://127.0.0.1:8000/api/items/')
        .then(response => {
          this.items = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
  mounted() {
    this.fetchItems();
  }
}
</script>

