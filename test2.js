const debounce = (func) => {
  let timer;

  return (e) => {
    if (timer) {
      clearTimeout(timer)
    }
    timer = setTimeout(func(e),500);
  };
};
