import React, { useEffect } from 'react';
import axios from 'axios';

const HomePage = () => {
  useEffect(()=> {
    async function getTrendingMusic() {
      const response = await axios.get('http://ec2-18-218-172-173.us-east-2.compute.amazonaws.com:8000', {
        headers: {
          'Access-Control-Allow-Origin': '*',
        },
      });
      console.log(response);
    }
    getTrendingMusic();
  }, []);
  return (
    <div>
    </div>
  );
};

export default HomePage;
