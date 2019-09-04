<template>
  <div lass="app-container">
    <el-table :data="list" v-loading="listLoading" element-loading-text="Loading" border fit highlight-current-row>
      <el-table-column align="center" label='ID' width="95">
        <template slot-scope="scope">  
          {{scope.row.id}}
        </template>
      </el-table-column>

      <el-table-column align="center" label='username' width="95">
        <template slot-scope="scope">
          {{scope.row.username}}
        </template>
      </el-table-column>
      <el-table-column align="center" label='password' width="900">
        <template slot-scope="scope">
          {{scope.row.password}}
        </template>
      </el-table-column>

    </el-table>  
  </div>
  
</template>

<script>
import { getList } from '@/api/table'

export default {
  data() {
    return {
      list: null,
      listLoading: true
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      // this.listLoading = false
      getList().then(response => {
        this.list = response.data[0]
        this.listLoading = false
      })
    }
  }
}
</script>
