export function format(source, params) {
  if (arguments.length == 0)
    return null;
  let str = arguments[0];
  for (let i = 1; i < arguments.length; i++)
  {
    let re = new RegExp('\\{' + (i - 1) + '\\}', 'gm');
    str = str.replace(re, arguments[i]);
  }
  return str;
}
