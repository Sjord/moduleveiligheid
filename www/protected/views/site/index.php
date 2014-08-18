<?php
/* @var $this SiteController */

$this->pageTitle=Yii::app()->name;
?>

Hier moet je je e-mail adres opgeven. Je krijgt dan een e-mail met een geheime link, en daar kan je dan de vragen invullen.

<a href="<?php echo $this->createUrl('chapter/view'); ?>">Beginnen</a>
