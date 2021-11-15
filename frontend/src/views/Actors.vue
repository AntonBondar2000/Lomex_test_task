<template>
  <main>
      <table class="main__table">
          <thead>
              <tr>
                  <th>Имя актера</th>
                  <th>Кол-во фильмов с участием актера</th>
                  <th>Жанр с лучшим средним рейтингом</th>
              </tr>
          </thead>
          <tbody>
              <tr v-for="item, index in actors" :key="index">
                  <td>{{item['name']}}</td>
                  <td>{{item['movies_count']}}</td>
                  <td>{{item['best_genre']}}</td>
              </tr>
          </tbody>
      </table>
  </main>
  <div class="pagination">
      <p>Всего страниц: {{allPages}}</p>
      <div class="pagination__nav">
        <button :disabled="!prev_page" @click="getPrevPage()">Предыдущая</button>
        <p>Текущая страница: {{currentPage}}</p>
        <button :disabled="!next_page" @click="getNextPage()">Следующая</button>
      </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
    name: 'Actors',
    data() {
        return {
            actors: [],
            next_page: null,
            prev_page: null,
            currentPage: 1,
            allPages: null
        }
    },
    methods:{
        getNextPage(){
            this.getActors(this.next_page)
            this.currentPage += 1
        },
        getPrevPage(){
            this.getActors(this.prev_page)
            this.currentPage -= 1
        },
        getActors(url){
            axios.get(url).then(response=>{
                this.actors = response.data.results
                this.next_page=response.data.next
                this.prev_page = response.data.previous
                this.allPages = Math.ceil(response.data.count / 20)
            })
        }
    },
    mounted(){
        this.getActors('http://localhost:8081/api/actors/')
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
    .pagination{
        display: flex;
        margin-top: 10px;
        justify-content: flex-end;
        align-items: center;
        width: 100%;
        &__nav{
            margin-left: 25px;
            display: flex;
            button{
                padding: 7px 15px;
                outline: none;
                background-color: white;
                font-size: 14px;
                border-radius: 7px;
                border: 1px solid rgb(159, 135, 235);
                transition-duration: .3s;
                &:not(:disabled){
                    cursor: pointer;
                }
                &:not(:disabled):hover{
                    background-color: rgb(159, 135, 235);
                    color: white
                }
            }
            p{
                padding: 5px 10px;
                margin: 0;
            }
        }
    }    
</style>