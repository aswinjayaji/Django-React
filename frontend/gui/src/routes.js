import React from 'react';
import { Route } from 'react-router-dom';
import Articlelist from './containers/ArticleListView';
import ArticleDetail from './containers/ArticleDetailView';

const BaseRouter=() =>(
<div>
    <Route exact path='/' component= {Articlelist}/>
    <Route exact path='/:articleID' component= {ArticleDetail}/>
    </div>
);

export default BaseRouter;