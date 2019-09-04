import request from '@/utils/request'

export function createuser(username, password, role) {
  return request({
    url: '/user/createuser/',
    method: 'post',
    data: {
      username,
      password,
      role
    }
  })
}
