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
      axios.get('http://10.110.0.110:8000/api/items/')
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

