// const fetch = require('node-fetch'); 
import offices from './data.js';

function main() {
  const markers = [];
  
  offices.forEach(office => {
    const marker = {
      address: office.name,
      coordinate: office.coordinates ? office.coordinates.split(' ').map(c => +c).reverse() : null,
      processed: office.processed
    };
  
    markers.push(marker);
  });

  return markers;
}

export { main };
