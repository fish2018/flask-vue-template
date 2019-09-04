<template>
  <div class="app-container">
    <el-form ref="createform"
             :model="createform"
             label-width="80px">
      <el-form-item>
        <el-input v-model="createform.username"
                  style="width: 300px">
          <template slot="prepend">用户名</template>
        </el-input>
      </el-form-item>

      <el-form-item>
        <el-input v-model="createform.password"
                  style="width: 300px"
                  type="password">
          <template slot="prepend">密码&#12288;</template>
        </el-input>
      </el-form-item>

      <el-form-item>
        <el-input v-model="createform.role"
                  style="width: 300px">
          <template slot="prepend">角色&#12288;</template>
        </el-input>
      </el-form-item>

      <el-form-item>
        <el-button type="primary"
                   @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>

export default {
  name: 'createuser',
  data() {
    return {
      createform: {
        username: '',
        password: '',
        role: ''
      }
    }
  },
  methods: {
    onSubmit() {
      this.$store.dispatch('Createuser', this.createform).then(() => {
        this.$router.push({ path: '/example/table' })
      }).catch(() => {
        this.loading = false
      })
      this.$message(this.createform.username + '用户已创建成功')
    },
    onCancel() {
      this.$message({
        message: 'cancel!',
        type: 'warning'
      })
    }
  }
}
</script>

<style scoped>
</style>
