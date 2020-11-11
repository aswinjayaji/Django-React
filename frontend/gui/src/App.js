import React from 'react';
import './App.css';
import 'antd/dist/antd.css';
import CustomLayout from './containers/Layout';
import Articlelist from './containers/ArticleListView';

function App() {
  return (
    <div className="App">
      <CustomLayout>
        <Articlelist/>
      </CustomLayout>
    </div>
  );
}

export default App;
