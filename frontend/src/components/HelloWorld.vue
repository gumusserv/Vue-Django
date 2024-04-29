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
      axios.get('http://10.181.91.67:8000/api/items/')
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

