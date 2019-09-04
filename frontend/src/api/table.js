import request from '@/utils/request'

export function getList() {
  return request({
    url: '/users/',
    method: 'get'
  })
}
