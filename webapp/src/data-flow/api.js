import forge from 'mappersmith'

export default forge({
  host: '',
  resources: {
    Account: {
      find: { path: '/account' },
    },
    Adoption: {
        find: { path: '/account' },
    },
    Animal: {
        find: { path: '/animal' },
    }
  }
})