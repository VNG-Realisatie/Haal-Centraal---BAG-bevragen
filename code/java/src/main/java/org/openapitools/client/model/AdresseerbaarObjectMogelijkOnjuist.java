/*
 * Huidige bevragingen API
 * Deze API levert actuele gegevens over adressen, adresseerbare objecten en panden. Actueel betekent in deze API `zonder eindstatus`. De bron voor deze API is de basisregistratie adressen en gebouwen (BAG).
 *
 * The version of the OpenAPI document: 1.2.0
 * Contact: bag@kadaster.nl
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Wanneer true is de waarde mogelijk onjuist en wordt juistheid op dit moment onderzocht. Zie toelichting.
 */
@ApiModel(description = "Wanneer true is de waarde mogelijk onjuist en wordt juistheid op dit moment onderzocht. Zie toelichting.")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2021-07-13T10:42:05.060374Z[Etc/UTC]")
public class AdresseerbaarObjectMogelijkOnjuist {
  public static final String SERIALIZED_NAME_GEBRUIKSDOELEN = "gebruiksdoelen";
  @SerializedName(SERIALIZED_NAME_GEBRUIKSDOELEN)
  private Boolean gebruiksdoelen;

  public static final String SERIALIZED_NAME_GEOMETRIE = "geometrie";
  @SerializedName(SERIALIZED_NAME_GEOMETRIE)
  private Boolean geometrie;

  public static final String SERIALIZED_NAME_NUMMERAANDUIDING_IDENTIFICATIES = "nummeraanduidingIdentificaties";
  @SerializedName(SERIALIZED_NAME_NUMMERAANDUIDING_IDENTIFICATIES)
  private Boolean nummeraanduidingIdentificaties;

  public static final String SERIALIZED_NAME_PAND_IDENTIFICATIES = "pandIdentificaties";
  @SerializedName(SERIALIZED_NAME_PAND_IDENTIFICATIES)
  private Boolean pandIdentificaties;

  public static final String SERIALIZED_NAME_OPPERVLAKTE = "oppervlakte";
  @SerializedName(SERIALIZED_NAME_OPPERVLAKTE)
  private Boolean oppervlakte;

  public static final String SERIALIZED_NAME_STATUS = "status";
  @SerializedName(SERIALIZED_NAME_STATUS)
  private Boolean status;

  public static final String SERIALIZED_NAME_TOELICHTING = "toelichting";
  @SerializedName(SERIALIZED_NAME_TOELICHTING)
  private List<String> toelichting = null;


  public AdresseerbaarObjectMogelijkOnjuist gebruiksdoelen(Boolean gebruiksdoelen) {
    
    this.gebruiksdoelen = gebruiksdoelen;
    return this;
  }

   /**
   * Get gebruiksdoelen
   * @return gebruiksdoelen
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getGebruiksdoelen() {
    return gebruiksdoelen;
  }


  public void setGebruiksdoelen(Boolean gebruiksdoelen) {
    this.gebruiksdoelen = gebruiksdoelen;
  }


  public AdresseerbaarObjectMogelijkOnjuist geometrie(Boolean geometrie) {
    
    this.geometrie = geometrie;
    return this;
  }

   /**
   * Get geometrie
   * @return geometrie
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getGeometrie() {
    return geometrie;
  }


  public void setGeometrie(Boolean geometrie) {
    this.geometrie = geometrie;
  }


  public AdresseerbaarObjectMogelijkOnjuist nummeraanduidingIdentificaties(Boolean nummeraanduidingIdentificaties) {
    
    this.nummeraanduidingIdentificaties = nummeraanduidingIdentificaties;
    return this;
  }

   /**
   * Get nummeraanduidingIdentificaties
   * @return nummeraanduidingIdentificaties
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getNummeraanduidingIdentificaties() {
    return nummeraanduidingIdentificaties;
  }


  public void setNummeraanduidingIdentificaties(Boolean nummeraanduidingIdentificaties) {
    this.nummeraanduidingIdentificaties = nummeraanduidingIdentificaties;
  }


  public AdresseerbaarObjectMogelijkOnjuist pandIdentificaties(Boolean pandIdentificaties) {
    
    this.pandIdentificaties = pandIdentificaties;
    return this;
  }

   /**
   * Get pandIdentificaties
   * @return pandIdentificaties
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getPandIdentificaties() {
    return pandIdentificaties;
  }


  public void setPandIdentificaties(Boolean pandIdentificaties) {
    this.pandIdentificaties = pandIdentificaties;
  }


  public AdresseerbaarObjectMogelijkOnjuist oppervlakte(Boolean oppervlakte) {
    
    this.oppervlakte = oppervlakte;
    return this;
  }

   /**
   * Get oppervlakte
   * @return oppervlakte
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getOppervlakte() {
    return oppervlakte;
  }


  public void setOppervlakte(Boolean oppervlakte) {
    this.oppervlakte = oppervlakte;
  }


  public AdresseerbaarObjectMogelijkOnjuist status(Boolean status) {
    
    this.status = status;
    return this;
  }

   /**
   * Get status
   * @return status
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getStatus() {
    return status;
  }


  public void setStatus(Boolean status) {
    this.status = status;
  }


  public AdresseerbaarObjectMogelijkOnjuist toelichting(List<String> toelichting) {
    
    this.toelichting = toelichting;
    return this;
  }

  public AdresseerbaarObjectMogelijkOnjuist addToelichtingItem(String toelichtingItem) {
    if (this.toelichting == null) {
      this.toelichting = new ArrayList<>();
    }
    this.toelichting.add(toelichtingItem);
    return this;
  }

   /**
   * Get toelichting
   * @return toelichting
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<String> getToelichting() {
    return toelichting;
  }


  public void setToelichting(List<String> toelichting) {
    this.toelichting = toelichting;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AdresseerbaarObjectMogelijkOnjuist adresseerbaarObjectMogelijkOnjuist = (AdresseerbaarObjectMogelijkOnjuist) o;
    return Objects.equals(this.gebruiksdoelen, adresseerbaarObjectMogelijkOnjuist.gebruiksdoelen) &&
        Objects.equals(this.geometrie, adresseerbaarObjectMogelijkOnjuist.geometrie) &&
        Objects.equals(this.nummeraanduidingIdentificaties, adresseerbaarObjectMogelijkOnjuist.nummeraanduidingIdentificaties) &&
        Objects.equals(this.pandIdentificaties, adresseerbaarObjectMogelijkOnjuist.pandIdentificaties) &&
        Objects.equals(this.oppervlakte, adresseerbaarObjectMogelijkOnjuist.oppervlakte) &&
        Objects.equals(this.status, adresseerbaarObjectMogelijkOnjuist.status) &&
        Objects.equals(this.toelichting, adresseerbaarObjectMogelijkOnjuist.toelichting);
  }

  @Override
  public int hashCode() {
    return Objects.hash(gebruiksdoelen, geometrie, nummeraanduidingIdentificaties, pandIdentificaties, oppervlakte, status, toelichting);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AdresseerbaarObjectMogelijkOnjuist {\n");
    sb.append("    gebruiksdoelen: ").append(toIndentedString(gebruiksdoelen)).append("\n");
    sb.append("    geometrie: ").append(toIndentedString(geometrie)).append("\n");
    sb.append("    nummeraanduidingIdentificaties: ").append(toIndentedString(nummeraanduidingIdentificaties)).append("\n");
    sb.append("    pandIdentificaties: ").append(toIndentedString(pandIdentificaties)).append("\n");
    sb.append("    oppervlakte: ").append(toIndentedString(oppervlakte)).append("\n");
    sb.append("    status: ").append(toIndentedString(status)).append("\n");
    sb.append("    toelichting: ").append(toIndentedString(toelichting)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

