<template>
    <main>
        <table class="main__table">
            <thead>
                <tr>
                    <th>Имя режисера</th>
                    <th>Актеры, встречающиеся, чаще всего</th>
                    <th>Лучшие фильмы режисера</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item, index in directors" :key="index">
                    <td>{{item['director']}}</td>
                    <td>
                        <p 
                            v-for="movie, idx in item['best_movies']" 
                            :key="idx"
                        >
                            {{movie}}
                        </p>
                    </td>
                    <td>
                        <p 
                            v-for="actors, idx in item['favourite_actors']" 
                            :key="idx"
                        >
                            {{actors[0]}} - {{actors[1]}}
                        </p>
                    </td>
                </tr>
            </tbody>
        </table>
    </main>     
</template>

<script>

import axios from 'axios'

export default {
    name: 'Directors',
    data() {
        return {
            directors: [],
        }
    },
    methods:{
        getDirectors(url){
            axios.get(url).then(response=>{
                this.directors = response.data
            })
        }
    },
    mounted(){
        this.getDirectors('http://localhost:8081/api/directors/')
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