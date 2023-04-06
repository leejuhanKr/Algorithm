function *zip (...iterables){
  let iterators = iterables.map(i => i[Symbol.iterator]() )
  while (true) {
      let results = iterators.map(iter => iter.next() )
      if (results.some(res => res.done) ) return
      else yield results.map(res => res.value )
  }
}