<template>
  <main>
      <table class="main__table">
          <thead>
              <tr>
                  <th>Название жанра</th>
                  <th>Кол-во фильмов жанра</th>
                  <th>Средняя оценка фильмов жанра</th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="item, index in genres" :key="index">
                  <td>{{item['genre']}}</td>
                  <td>{{item['movies_count']}}</td>
                  <td>{{item['avg_rating']}}</td>
              </tr>
          </tbody>
      </table>
  </main>
</template>

<script>

import axios from 'axios'

export default {
    name: 'Genres',
    data() {
        return {
            genres: [],
        }
    },
    methods:{
        getGenres(url){
            axios.get(url).then(response=>{
                this.genres = response.data
            })
        }
    },
    mounted(){
        this.getGenres('http://localhost:8081/api/genres/')
    }

}
</script>

<style scoped lang="scss">
    .main__table{
        width: 100%;
        border-collapse: collapse;
        border: 1px solid black;
        thead{
            border-bottom: 1px solid black;
            th{
                padding: 10px 15px;
                border: 1px solid black;
                background-color: #ebe7e7;
                font-weight: bold;
            }
        }
        tbody{
            td{
                padding: 10px 15px;
                border: 1px solid black;
            }
        }
    }
</style>